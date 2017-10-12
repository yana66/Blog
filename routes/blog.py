from . import *
import pymongo
main = Blueprint('home', __name__)


@main.route('/')
def index():
    offset = request.args.get('offset')
    limit = request.args.get('limit')
    if offset or limit is not None:
        offset = int(offset)
        limit = int(limit)
    else:
        offset = 1
        limit = 5
    posts = Post.find(flag=pymongo.DESCENDING)
    total = posts.count()
    posts = posts[offset-1:].limit(limit)
    old_start = offset + limit
    new_start = offset - limit
    o_url = True
    n_url = True
    if old_start > total:
        old_start -= limit
        o_url = False
    if new_start < 1:
        new_start = 1
        n_url = False
    older_url = '/?offset={}&limit={}'.format(old_start, limit)
    newer_url = '/?offset={}&limit={}'.format(new_start, limit)
    return render_template('index.html', posts=posts, older_url=older_url, newer_url=newer_url, o_url=o_url, n_url=n_url)


@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/contact')
def contact():
    return render_template('contact.html')


# 写博客
@main.route('/add')
@admin_required
def add():
    return render_template('add.html')


# 提交新博客
@main.route('/new', methods=['POST'])
@admin_required
def new():
    Post.new(request.form)
    return redirect(url_for('.index'))


@main.route('/edit/<title>')
@admin_required
def edit(title):
    m = Post.find_one(title=title)
    return render_template('edit.html', post=m)


@main.route('/update/<title>', methods=['POST'])
@admin_required
def update(title):
    Post.update(request.form, title=title)
    return redirect(url_for('.detail', title=title))


@main.route('/delete/<title>')
@admin_required
def delete(title):
    Post.delete(title=title)
    return redirect(url_for('.index'))


# 博客详细
@main.route('/post/<title>')
def detail(title):
    m = Post.find_one(title=title)
    return render_template('post.html', post=m)


# 注册登录
@main.route('/auth')
def auth():
    return render_template('auth.html')


@main.route('/login', methods=['POST'])
def login():
    form = request.form
    user = User.login(form)
    if user:
        session['username'] = user['username']
        session.permanent = True
        return redirect(url_for('.index'))
    return redirect(url_for('.auth'))


@main.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        if User.register(request.form):
            return redirect(url_for('.auth'))
        else:
            return redirect(url_for('register'))
    return render_template('register.html')

