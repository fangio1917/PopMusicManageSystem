<template>
  <div class="q-pa-md">
    <div class="login_box column" style="max-width: 300px">
      <p class="text-h5 text-center">添加歌曲</p>
      <q-input v-model="name" label="歌曲名" placeholder="请输入歌曲名"/>
       <q-input v-model="singer" label="歌手" placeholder="请输入歌手名"/>
       <q-input v-model="album" label="专辑" placeholder="请输入专辑名"/>

       <q-input filled v-model="date">
          <template v-slot:prepend>
            <q-icon name="event" class="cursor-pointer">
              <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                <q-date v-model="date" mask="YYYY-MM-DD HH:mm">
                  <div class="row items-center justify-end">
                    <q-btn v-close-popup label="Close" color="primary" flat />
                  </div>
                </q-date>
              </q-popup-proxy>
            </q-icon>
          </template>

          <template v-slot:append>
            <q-icon name="access_time" class="cursor-pointer">
              <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                <q-time v-model="date" mask="YYYY-MM-DD HH:mm" format24h>
                  <div class="row items-center justify-end">
                    <q-btn v-close-popup label="Close" color="primary" flat />
                  </div>
                </q-time>
              </q-popup-proxy>
            </q-icon>
          </template>
      </q-input>

      <q-file
        v-model="files"
        label="Pick files"
        filled
        counter
        :counter-label="counterLabelFn"
        max-files="3"
        multiple
        style="max-width: 300px"
        @update:model-value="add_file"
      >
        <template v-slot:prepend>
          <q-icon name="attach_file" />
        </template>
      </q-file>
      <q-btn color="white" text-color="black" label="添加" @click="add" />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router'
// 定义组件名称
defineOptions({
  name: 'SongAddPage'
});

const files = ref(null)


// 定义响应式数据
const name = ref('');
const singer = ref('');
const album = ref('');
const date = ref('2002-12-13 13:00');
const url = ref('music/');
const user_token = window.localStorage.getItem('token')
const router = useRouter()



const add = async () => {

  try {
        const response = await axios.post('http://localhost:9000/api/songs/add', {
          name: name.value,
          singer: singer.value,
          album: album.value,
          date: date.value,
          url: url.value
        },{
          headers: {
            'Authorization': `Bearer ${user_token}`
          }
        })

        if (response.data.success) {
          console.log(response.data.message)
          alert('添加成功')
          await router.push('/songs')
        } else {
          alert('Fetching songs failed: ' + response.data.message)
        }
      } catch (error) {
        console.error('Error fetching song:', error)
        alert('An error occurred during fetching song')
      }
};

const add_file = async () => {

  try {
        const response = await axios.post('http://localhost:8000/api/file/upload', {
          file: files.value
        },{
          headers: {
            'Authorization': `Bearer ${user_token}`,
            'Content-Type': 'multipart/form-data'
          }
        })

        if (response.data.success) {
          console.log(response.data.message)
          alert('添加成功')
        } else {
          alert('Fetching songs failed: ' + response.data.message)
        }
      } catch (error) {
        console.error('Error fetching song:', error)
        alert('An error occurred during fetching song')
      }
};
const counterLabelFn = ({ totalSize, filesNumber, maxFiles })=> {
        return `${filesNumber} files of ${maxFiles} | ${totalSize}`
};
</script>

<style>
.login_box {
  margin-left: 40%;
  margin-top: 10%;
}
</style>
