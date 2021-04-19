### 1. vue指令
> 带有v前缀的特殊属性(也就是作为属性插入DOM元素中使用)，它值为单个表达式（表达式标量一般为vue实例中的数据属性）。
> 作用：当表达式的值发生改变，将变化反映到DOM上。（体现了数据驱动的思想，vue让你只关注数据，不用你来操作DOM元素）
### 2. vue指令 带参数：
> - 一般的指令后面可以带从参数，在指令冒号后面加参数   <code><div v-bind:href="url">帅哥</div></code>
>
> - 动态指令： 
>
> ```js
> <a v-bind:[attribute]="url" >百度一下 </a>
> // 不要使用大写，因为浏览器会将元素属性名的大写全部强制转为小写字符
> // 不要使用复杂的表达式,要遵守HTML属性命名的规范 
> ```

### 3. vue中两种数据绑定的方式

1. 文本插值
2. 元素属性，v指令绑定


#### 4. 常见指令的作用

- <code style="font-size:14px;padding:10px 20px;color:red;"> v-show</code>

  ```js
    <div id="app">
          <h1 v-show="yes">Yes!</h1>
          <h1 v-show="no">No!</h1>
          <h1 v-show="age >= 25">Age: {{age}}</h1>
          <h1 v-show="name.indexOf('Smith') >= 0">Name:{{name}}</h1>
      </div>
      <script src="../node_modules/vue/dist/vue.js"></script>
      <script>
          var app = new Vue({
              el: "#app",
              data: {
                  yes: true,
                  no: false,
                  age: 28,
                  name: "Will Smith"
              },
              methods: {
                  // 放置方法
              }
          });
      <script>
  ```

  > - **核心原理：**
  >   ```css display:none;```
  >   也就是所，设置v-show指令的元素，vue会根据其表达式值的真假，来设置css属性display来控制该元素的显示与隐藏, 同时也说明该元素本身一定是被渲染到DOM Tree上的（区别v-if|v-else|v-else-if）
  > - **技巧template**
  >   如果要控制多个元素的显示与隐藏，则可以使用template标签将元素“装起来”
  >
  > ```js
  > <template v-show="flag">
  > 	<div>item 1</div>
  > 	<div>item 2</div>
  > </template>
  > ```
  >
  > 

<!-- v-show指令详解 -->

- <code style="font-size:14px;padding:10px 20px;color:red;">v-if|v-else-if|v-else</code>
  
  ```js
  <body>
    <div id="app">
        <div>你的分数:{{score}}</div>
        <span v-if="score >= 85">优秀</span>
        <span v-else-if="score >= 85">良好</span>
        <span v-else-if="score >= 85">及格</span>
        <span v-else>不及格</span>
    </div>
    <script src="../node_modules/vue/dist/vue.js"></script>
    <script>
        const app = new Vue({
            el: "#app",
            data: {
                score: 90
            }
        });
    </script>
</body>
  ```
  
  > **核心原理：**
  >
  > **根据表达式的值来确定是否将元素加入DOM Tree**



### 区别

1.  <code style="font-size:14px;padding:10px 20px;color:red;">v-if|v-else-if|v-else</code>根据表达式的值来决定是否将元素加入DOM Tree
2.  <code style="font-size:14px;padding:10px 20px;color:red;">v-show</code>根据表达式的值来决定是否将元素隐藏 display:none; （元素会加入DOM Tree，是否显示由表达式值确定）



### 总结

​	首先介绍了vue的指令概念，形式：v-指令。 指令以HTML属性的形式加入，指令的值为：JavaScript表达式（表达式整体有一个值）。

然后介绍了 v-show和v-if|v-else-if|v-else 来控制元素的显示和隐藏的功能，以及他们之间的差别

### 参考
    - 《Vue.js从入门到实战》-孙鑫


