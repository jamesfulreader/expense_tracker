<script setup lang="ts">
type Transaction = {
  id: number
  text: string
  amount: number
}

const transactions: Transaction[] = [
  { id: 1, text: 'Dog food', amount: -59.99 },
  { id: 2, text: 'Paycheck', amount: 650.9 },
  { id: 3, text: 'Groceries', amount: -42.87 }
]
</script>

<template>
  <h3>History</h3>
  <ul id="list" class="list">
    <li
      v-for="transaction in transactions"
      :key="transaction.id"
      :class="transaction.amount < 0 ? 'minus' : 'plus'"
    >
      {{ transaction.text }} <span>${{ transaction.amount }}</span
      ><button class="delete-btn">x</button>
    </li>
  </ul>
</template>
