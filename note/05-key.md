### Vue复用元素模板中使用相同的元素，为了提高渲染效率。如果给每个元素设置唯一的key属性，可以告诉Vue，这两个元素完全独立，不要复用。

### 举个例子：

1. 没有设置key，发现复用input元素，输入的用户名在email中出现
```js
<div id="app">
        <template v-if="loginType == 'username'">
            <label >用户名:</label>
            <input key="username-input" placeholder="请输入你的用户名">
        </template>
        <template v-else>
            <label >Email:</label>
            <input placeholder="请输入你的Email">
        </template>
        <p>
            <button @click="changeLoginType">切换登入模式</button>
        </p>
    </div>
    <script src="../node_modules/vue/dist/vue.js"></script>
    <script>
        const app = new Vue({
            el: "#app",
            data: {
                loginType: "username"
            },
            methods: {
                changeLoginType() {
                    if (this.loginType === 'username') {
                        this.loginType = 'email'
                    } else {
                        this.loginType = 'username';
                    }
                }
            }
        });
    </script>
</body>
```

2. 设置key值不要复用

```js
<div id="app">
     <template v-if="loginType == 'username'">
         <label >用户名:</label>
         <input placeholder="请输入你的用户名">
     </template>
     <template v-else>
         <label >Email:</label>
         <input placeholder="请输入你的Email" key="email-input">
     </template>
     <p>
         <button @click="changeLoginType">切换登入模式</button>
     </p>
 </div>
 <script src="../node_modules/vue/dist/vue.js"></script>
 <script>
     const app = new Vue({
         el: "#app",
         data: {
             loginType: "username"
         },
         methods: {
             changeLoginType() {
                 if (this.loginType === 'username') {
                     this.loginType = 'email'
                 } else {
                     this.loginType = 'username';
                 }
             }
         }
     });
 </script>
</body>
```




### 属性key的值
> 预期： number|string|boolean|symbol
> 主要用在Vue的虚拟DOM算法中（这个目前我也不怎么了解，学到后期我会专门一个博文）



### 应用

> 未接触到实际的应用,正在努力学习中,以下两个是摘抄自Vue官方文档

- 完整地触发组件的生命周期钩子
- 触发过渡



### 参考

- vue官方文档
- 《Vue.js深入浅出》 孙鑫