<template>
<!--  <div class="q-pa-md">-->
<!--    <div class="q-gutter-y-md column" style="max-width: 300px ">-->
  <div class="q-pa-md">
    <div class="longin_box" style="max-width: 300px ">
      <q-input v-model="ph" label="用户名" placeholder="请输入用户名" hint="username" class="longin_box"  />
      <q-input v-model="password" label="密码" filled type="password" placeholder="请输入密码"  hint="Password" />
    <!--      <q-input v-model="password" label="密码" placeholder="请输入您的密码"  filled :type="isPwd ? 'password' : 'text'" hint="Password with toggle">-->
    <!--          <template v-slot:append>-->
    <!--            <q-icon-->
    <!--              :name="isPwd ? 'visibility_off' : 'visibility'"-->
    <!--              class="cursor-pointer"-->
    <!--              @click="isPwd = !isPwd"-->
    <!--            />-->
    <!--          </template>-->
    <!--        </q-input>-->

    </div>
  </div>
<!--    </div>-->
<!--  </div>-->
</template>


<script>
import { ref } from 'vue'

export default {
  setup () {
    return {
      text: ref(''),
      ph: ref(''),
      password: ref(''),
      isPwd: ref(true),
      dense: ref(false)
    }
  }
}
</script>

<script setup>
defineOptions({
  name: 'IndexPage'
});
</script>
