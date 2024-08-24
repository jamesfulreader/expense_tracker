<script setup lang="ts">
import { reactive } from 'vue'
import axios from 'axios'

const form = reactive({
  title: '',
  amount: ''
})

const handleSubmit = async () => {
  const newEntry = {
    title: form.title,
    amount: form.amount
  }

  try {
    const response = await axios.post('http://127.0.0.1:8000/api/entry/', newEntry)
    form.title = ''
    form.amount = ''
  } catch (error) {
    console.error('Error posting entry: ', error)
  }
}
</script>
<template>
  <h3>Add new transaction</h3>
  <form id="form" @submit.prevent="handleSubmit">
    <div class="form-control">
      <label for="text">Text</label>
      <input type="text" id="text" placeholder="Enter text..." v-model="form.title" />
    </div>
    <div class="form-control">
      <label for="amount"
        >Amount <br />
        (negative - expense, positive - income)</label
      >
      <input
        type="number"
        step="0.01"
        id="amount"
        placeholder="Enter amount..."
        v-model="form.amount"
      />
    </div>
    <button class="btn">Add transaction</button>
  </form>
</template>
