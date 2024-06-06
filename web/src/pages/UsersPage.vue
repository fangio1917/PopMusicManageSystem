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
        <q-btn color="primary" :disable="loading" label="增加用户" @click="addRow" />
        <q-btn class="q-ml-sm" color="primary" :disable="loading" label="删除用户" @click="removeRow" />
        <q-btn class="q-ml-sm" color="primary" :disable="loading" label="修改用户" @click="modifyRow" />
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
    label: 'ID',
    align: 'center',
    field: row => row.id,
    format: val => `${val}`,
    sortable: true
  },
  {
    name: 'name',
    required: true,
    label: '姓名',
    align: 'center',
    field: row => row.name,
    format: val => `${val}`,
    sortable: true
  },
  {
    name: 'permission',
    required: true,
    label: '权限',
    align: 'center',
    field: row => row.permission,
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
        router.push('/users/add')
      },

      removeRow() {
       router.push('/users/delete')
      },

      modifyRow(){
        router.push('/users/modify')
      }
    }
  }
}
</script>
