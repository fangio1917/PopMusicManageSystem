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
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

export default {
  setup() {
    const loading = ref(false)
    const filter = ref('')
    const rows = ref([])

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

    const user_token = window.localStorage.getItem('token')

    const getSongs = async () => {
      console.log('Fetching users...')
      try {
        const response = await axios.get('http://localhost:9000/api/songs/query', {
          headers: {
            'Authorization': `Bearer ${user_token}`
          }
        })

        if (response.data.success) {
          console.log(response.data)
          rows.value = response.data.data // Assign data directly to rows
        } else {
          alert('Fetching users failed: ' + response.data.message)
        }
      } catch (error) {
        console.error('Error fetching users:', error)
        alert('An error occurred during fetching users')
      }
    }

    onMounted(() => {
      getSongs()
    })

    const router = useRouter()

    const addRow = () => {
      router.push('/songs/add')
    }

    const removeRow = () => {
      router.push('/songs/delete')
    }

    const modifyRow = () => {
      router.push('/songs/modify')
    }

    return {
      columns,
      rows,
      loading,
      filter,
      addRow,
      removeRow,
      modifyRow
    }
  }
}
</script>
