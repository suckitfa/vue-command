### v-for
> 作用： 遍历数组

### 使用方式
```html
<ul>
    <!-- 这里index是可选的，跟 forEach等迭代方法中的回到传参类似 -->
    <li v-for="(book,index) in books">{{book.name}}</li>
    <!-- 这里的of可以代替 in  ES6中的迭代语法-->
</ul>
```
### 完整例子
```html
<body>
    <div id="app">
        <ul>
            <li v-for="(book,index) in books">{{index}}{{book.title}}</li>
        </ul>
    </div>
    <script src="../node_modules/vue/dist/vue.js "></script>
    <script>
        const app = new Vue({
            el: "#app",
            data: {
                books: [{
                    title: "Vue无难事"
                }, {
                    title: "VC++深入详解"
                }, {
                    title: "Server/JSP深入详解"
                }]
            },
            methods: {

            },
        });
    </script>
</body>
```
### 渲染细节
> Vue在检测数组变化的时候，并不是直接重新渲染整个列表，而是最大化的复用DOM元素。替换数组中的，含有相同元素的项不会被重新渲染，因此**可以大胆的替换旧的数组**
> 关于Vue中的性能优化： Vue中含有虚拟元素，Virtual DOM，简单的看下大概是这样定义的。
```js
class VNode {
    constructor (tag, data, children, text, elm) {
        /*当前节点的标签名*/
        this.tag = tag;
        /*当前节点的一些数据信息，比如props、attrs等数据*/
        this.data = data;
        /*当前节点的子节点，是一个数组*/
        this.children = children;
        /*当前节点的文本*/
        this.text = text;
        /*当前虚拟节点对应的真实dom节点*/
        this.elm = elm;
    }
}
```
> 也就是说在保存了一份页面元素的"映射"（也就是Vue拿着小本本记着）,当数据更新的时候，Vue先将现在的数据和原来的数据对比（涉及到一个diff算法-我自己还没整明白）（Vue有着强大的小本本），只将改变了的数据更新导视图上！ 因此在上面说：**可以大胆的进行数组的替换。**


### 数组检测更新 数组变异方法 (mutation method)

> **mutations** a permanent change in an organism, or the changed organism itself
> 1. 以下方法会改变数组
>    - push
>    - pop
>    - shift
>    - unshift
>    - splice
>    - sort
>    - reverse
> 2. 以下方法不会改变原来的数组，(返回一个新的数组)
>   - fliter
>   - concat
>   - slice
> 3. Vue无法检测到数组数据更换,如下：
> ```js
> app.books[0] = {title:"《如何成为开发高手》"}
> app.books.length = 0;
> ```
> 解决方法就是：
> ```js
> ```

### 参考
    - 《Vue.js从入门到实战》
    - 掘金小册《剖析Vue.js内部运行机制》作者：染陌同学