<template>
  <div class="q-pa-md">
    <div class="login_box column" style="max-width: 300px">
      <p class="text-h5 text-center">修改歌曲</p>
      <q-input v-model="id" label="歌曲id" placeholder="请输入歌曲id"/>
      <q-input v-model="name" label="歌曲名" placeholder="请输入歌曲名"/>
       <q-input v-model="singer" label="歌手" placeholder="请输入歌手名"/>
       <q-input v-model="album" label="专辑" placeholder="请输入专辑名"/>
       <q-input v-model="data" label="日期" placeholder="格式为：2003-8-9 00:00:00"/>
       <q-input v-model="url" label="连接" placeholder="输入连接"/>
      <q-file
        v-model="files"
        label="Pick files"
        filled
        counter
        :counter-label="counterLabelFn"
        max-files="3"
        multiple
        style="max-width: 300px"
      >
        <template v-slot:prepend>
          <q-icon name="attach_file" />
        </template>
      </q-file>
      <q-btn color="white" text-color="black" label="修改" @click="modify" />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
// 定义组件名称
defineOptions({
  name: 'SongAddPage'
});

const files = ref(null)
// 定义响应式数据
const id = ref('');
const name = ref('');
const singer = ref('');
const album = ref('');
const data = ref('');
const url = ref('');
const user_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MjEwNjI0MzEsInN1YiI6ImZhbmdpbyJ9.JxBrcVh1cULWl4rd6ImB_KJomJA9BJDOzOJTALxOPjE'

const modify = async () => {
};
const counterLabelFn = ({ totalSize, filesNumber, maxFiles })=> {
        return `${filesNumber} files of ${maxFiles} | ${totalSize}`
};
</script>

<style>
.login_box {
  margin: 30%;
}
</style>
