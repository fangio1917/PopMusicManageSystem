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
      <template v-slot:top-left></template>
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

    const user_token = window.localStorage.getItem('token')

    const getUsers = async () => {
      console.log('Fetching users...')
      try {
        const response = await axios.get('http://localhost:9000/api/users/query', {
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
      getUsers()
    })

    const router = useRouter()

    const addRow = () => {
      router.push('/users/add')
    }

    const removeRow = () => {
      router.push('/users/delete')
    }

    const modifyRow = () => {
      router.push('/users/modify')
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
