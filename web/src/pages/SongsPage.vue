<template>
  <div class="q-pa-md">
    <q-table
      title="Treats"
      :rows="rows"
      :columns="columns"
      row-key="id"
      :filter="filter"
      :loading="loading"
    >

      <template v-slot:top-left>

      </template>

      <template v-slot:top>
        <q-btn color="primary" :disable="loading" label="增加歌曲" @click="addRow" />
        <q-btn class="q-ml-sm" color="primary" :disable="loading" label="删除歌曲" @click="removeRow" />
        <q-btn class="q-ml-sm" color="primary" :disable="loading" label="修改歌曲" @click="modifyRow" />
        <q-space />
        <q-input borderless dense debounce="300" color="primary" v-model="filter">
          <template v-slot:append>
            <q-icon name="search" />
          </template>
        </q-input>
      </template>

    </q-table>
  </div>
</template>

<script>
import { ref } from 'vue'
import {useRouter} from "vue-router";
import { mapActions } from 'vuex';
import axios from "axios";

const user_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MjEwNjI0MzEsInN1YiI6ImZhbmdpbyJ9.JxBrcVh1cULWl4rd6ImB_KJomJA9BJDOzOJTALxOPjE'

const columns = [
  {
    name: 'id',
    required: true,
    label: '编号',
    align: 'center',
    field: row => row.id,
    format: val => `${val}`,
    sortable: true
  },
  {
    name: 'name',
    required: true,
    label: '歌曲',
    align: 'center',
    field: row => row.name,
    format: val => `${val}`,
    sortable: true
  },
  {
    name: 'singer',
    required: true,
    label: '歌手',
    align: 'center',
    field: row => row.singer,
    format: val => `${val}`,
    sortable: true
  },
  {
    name: 'album',
    required: true,
    label: '专辑',
    align: 'center',
    field: row => row.album,
    format: val => `${val}`,
    sortable: true
  },
  {
    name: 'date',
    required: true,
    label: '日期',
    align: 'center',
    field: row => row.date,
    format: val => `${val}`,
    sortable: true
  },
  {
    name: 'url',
    required: true,
    label: '链接',
    align: 'center',
    field: row => row.url,
    format: val => `${val}`,
    sortable: true
  }
]

const originalRows = []

const getSongs = async () => {
  axios.get('https://localhost:8080/api/users/query',{
    headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + user_token
    }
  })
  .then(response => {
    console.log(response.data);
    originalRows.push(response.data);
  })
  .catch(error => {
    console.error(error);
  });
}

export default {
  setup() {
    const loading = ref(false)
    const filter = ref('')
    const rowCount = ref(10)
    const rows = ref([...originalRows])

    const router = useRouter();
    window.onload = function (){
      getSongs();
    }

    return {
      columns,
      rows,

      loading,
      filter,
      rowCount,


      // emulate fetching data from server

      getSongs,
      addRow() {
        router.push('/songs/add')
      },

      removeRow() {
       router.push('/songs/delete')
      },

      modifyRow(){
        router.push('/songs/modify')
      }
    }
  }
}
</script>
