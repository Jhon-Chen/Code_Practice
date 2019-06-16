from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://jhonchen:2553522375@47.100.200.127:3306/flask_practice'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
def index():
    return 'Hello World!'


if __name__ == "__main__":
    app.run(debug=True)
    # 更新现有数据库表的粗暴方式是先删除旧表再重新创建
    db.drop_all()
    db.create_all()
    # 下面这段代码创建了一些用户。
    admin_role = Role(name='Admin')
    mod_role = Role(name='Moderator')
    user_role = Role(name='User')
    user_jhon = User(username='jhon', role=admin_role)
    user_susan = User(username='susan', role=user_role)
    user_david = User(username='david', role=user_role)

    db.session.add_all([admin_role, mod_role, user_role, user_david, user_jhon, user_susan])
    db.session.commit()

    """修改行：在数据库会话上调用add()方法也能更新模型。下面把“Admin”重命名为“Administrator” """
    admin_role.name = 'Administrator'
    db.session.add(admin_role)
    db.session.commit()
    """删除行：数据库还有个delete()方法。下面把”Moderator“从数据库中删除"""
    db.session.delete(mod_role)
    db.session.commit()
    """查询行：Flask-SQLAlchemy为每个模型类都提供了query对象。最基本的模型查询是取回对应表中的所有记录"""
    Role.query.all()
    User.query.all()
    """使用过滤器可以配置query对象进行更精确的数据库查询。下面查找角色为“User”的所有用户"""
    User.query.filter_by(role=user_role).all()
    """若要查看SQLAlchemy为查询生成的原生SQL查询语句，只需要把query对象转换成字符串"""
    str(User.query.filter_by(role=user_role))
    """filter_by()等过滤器在query对象上调用，返回一个更精确的query对象。多个过滤器可以一起调用，知道获得所需结果
    过滤器：
    filter()                        把过滤器添加到原查询上，返回一个新的查询
    filter_by()                     把等值过滤器添加到原查询上，返回一个新查询
    limit()                         使用指定的值限制原查询返回的结果数量，返回一个新查询
    offset()                        偏移原查询返回的结果数量，返回一个新查询
    order_by()                      根据指定条件对原查询结果进行排序，返回一个新查询
    group_by()                      根据指定条件对原查询结果进行分组，返回一个新查询
    
    在查询上应用指定的过滤器后，通过调研all()执行查询，以列表的形式返回结果。除了all()之外，还有其他方法能触发查询执行。
    最常用的SQLAlchemy查询执行函数：
    all()                           以列表的形式返回查询的所有结果
    first()                         返回查询的第一个结果，如果没有结果，则返回None
    first_or_404()                  返回查询的第一个结果，如果没有结果，则终止请求，返回404错误响应
    get()                           返回指定主键对应的行，如果没有对应的行，则返回None
    get_or_404()                    返回指定主键对应的行，如果没找到指定的主键，则终止请求，返回404响应
    count()                         返回查询结果的数量
    paginate()                      返回一个Paginate对象，它包含指定范围内的结果
    
    user_role.users表达式时，隐含的查询会调用all()返回一个用户列表。query对象是隐藏的，因此无法指定更精确的查询过滤器。
    故而我们应该修改关系设置，加入 lazy = 'dynamic'参数，从而禁止自动执行查询
    这样配置关系之后，user_role.users会返回一个尚未执行的查询，因此可以在其上添加过滤器"""