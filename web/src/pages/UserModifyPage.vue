<template>
  <div class="q-pa-md">
    <div class="login_box column" style="max-width: 300px">
      <p class="text-h5 text-center">修改用户</p>
      <q-input v-model="id" label="用户编号" placeholder="请输入用户编号"/>
      <q-input v-model="name" label="用户名" placeholder="请输入用户名"/>
      <q-input v-model="password" label="密码" placeholder="用户密码"/>
      <q-input v-model="permission" label="用户权限" placeholder="1:root; 10:admin; 100:user"/>
      <q-btn color="white" text-color="black" label="修改" @click="add"/>
    </div>
  </div>
</template>

<script setup>
import {ref} from 'vue';
import axios from 'axios';
// 定义组件名称
defineOptions({
  name: 'SongAddPage'
});


// 定义响应式数据
const id = ref('');
const name = ref('');
const password = ref('');
const permission = ref('');
const user_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MjEwNjI0MzEsInN1YiI6ImZhbmdpbyJ9.JxBrcVh1cULWl4rd6ImB_KJomJA9BJDOzOJTALxOPjE'

const add = async () => {
};
</script>

<style>
.login_box {
  margin: 30%;
}
</style>
