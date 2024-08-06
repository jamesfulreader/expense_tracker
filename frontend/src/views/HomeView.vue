<script setup lang="ts">
import { RouterLink } from 'vue-router'
import HeaderComponent from '@/components/HeaderComponent.vue'
import BalanceComponent from '@/components/BalanceComponent.vue'
import IncomeExpenses from '@/components/IncomeExpenses.vue'
import TransactionList from '@/components/TransactionList.vue'
import AddTransaction from '@/components/AddTransaction.vue'
</script>

<template>
  <HeaderComponent />
  <div class="container">
    <BalanceComponent />
    <IncomeExpenses />
    <TransactionList />
    <AddTransaction />
  </div>
  <RouterLink to="/about"> About </RouterLink>
</template>
