<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md column center_box" style="max-width: 300px">

       <q-input
        v-model="inputModel"
        filled
        clearable
        color="purple-12"
        label="输入你要删除的用户"
        hint="确保输入的为数字"
        :shadow-text="inputShadowText"
        @keydown="processInputFill"
        @focus="processInputFill"
      />

     <q-btn @click="deleted_user" label="确认删除" />
    </div>
  </div>
</template>

<script>
import { event } from 'quasar'
import { ref, computed } from 'vue'
import axios from "axios";

const { stopAndPrevent } = event

export default {
  setup () {
    const inputModel = ref('')
    const inputFillCancelled = ref(false)
    const inputShadowText = computed(() => {
      if (inputFillCancelled.value === true) {
        return ''
      }

      const t = '输入你要删除的编号'
      const empty = typeof inputModel.value !== 'string' || inputModel.value.length === 0

      if (empty === true) {
        return t
      }
      else if (t.indexOf(inputModel.value) !== 0) {
        return ''
      }

      return t
        .split(inputModel.value)
        .slice(1)
        .join(inputModel.value)
    })
    const user_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MjEwNjI0MzEsInN1YiI6ImZhbmdpbyJ9.JxBrcVh1cULWl4rd6ImB_KJomJA9BJDOzOJTALxOPjE'
    const textareaModel = ref('')
    const textareaFillCancelled = ref(false)
    const textareaShadowText = computed(() => {
      if (textareaFillCancelled.value === true) {
        return ''
      }

      const
        t = 'This text\nwill be filled\non multiple lines\nwhen you press TAB',
        empty = typeof textareaModel.value !== 'string' || textareaModel.value.length === 0

      if (empty === true) {
        return t.split('\n')[ 0 ]
      }
      else if (t.indexOf(textareaModel.value) !== 0) {
        return ''
      }

      return t
        .split(textareaModel.value)
        .slice(1)
        .join(textareaModel.value)
        .split('\n')[ 0 ]
    })

    return {
      inputModel,
      inputFillCancelled,
      inputShadowText,

      deleted_user (){
         axios.get('https://localhost:8080/api/users/delete',{
          headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + user_token
          },
           params:{
            deleted_id: Number(inputModel.value)
           }
        })
        .then(response => {
          console.log(response.data);
        })
        .catch(error => {
          console.error(error);
        });
      },
      processInputFill (e) {
        if (e === void 0) {
          return
        }

        if (e.keyCode === 27) {
          if (inputFillCancelled.value !== true) {
            inputFillCancelled.value = true
          }
        }
        else if (e.keyCode === 9) {
          if (inputFillCancelled.value !== true && inputShadowText.value.length > 0) {
            stopAndPrevent(e)
            inputModel.value = (typeof inputModel.value === 'string' ? inputModel.value : '') + inputShadowText.value
          }
        }
        else if (inputFillCancelled.value === true) {
          inputFillCancelled.value = false
        }
      },

      textareaModel,
      textareaFillCancelled,
      textareaShadowText,


    }
  }
}
</script>

<style>
.center_box {
  margin: 30%;
}
</style>
