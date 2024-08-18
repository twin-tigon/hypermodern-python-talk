<script setup lang="ts">
import { ref, onMounted } from "vue";
import Chart from "primevue/chart";

onMounted(() => {
  chartData.value = setChartData();
  chartOptions.value = setChartOptions();
});

const chartData = ref();
const chartOptions = ref();

const setChartData = () => {
  const documentStyle = getComputedStyle(document.documentElement);

  return {
    labels: [
      "ReactJS",
      "TypeScript",
      "Python",
      "AWS",
      "Postgres",
      "JavaScript",
      "Go",
      "NodeJS",
      "Rust",
      "Kubernetes",
      "NextJS",
      "Terraform",
      "Elixir",
      "GCP",
      "Django",
      "SQL",
      "Docker",
      "NestJS",
      "Ruby",
      "Pytorch",
    ],
    datasets: [
      {
        label: "Technology Demand in Job Descriptions - 2024 (%)",
        backgroundColor: documentStyle.getPropertyValue("--p-cyan-500"),
        borderColor: documentStyle.getPropertyValue("--p-cyan-500"),
        data: [
          45, 40, 40, 29, 25, 14, 12, 12, 10, 10, 10, 7, 7, 7, 7, 7, 5, 5, 5, 5,
        ],
      },
    ],
  };
};
const setChartOptions = () => {
  const documentStyle = getComputedStyle(document.documentElement);
  const textColor = documentStyle.getPropertyValue("--p-text-color");
  const textColorSecondary = documentStyle.getPropertyValue(
    "--p-text-muted-color"
  );
  const surfaceBorder = documentStyle.getPropertyValue(
    "--p-content-border-color"
  );

  return {
    maintainAspectRatio: false,
    aspectRatio: 0.8,
    plugins: {
      legend: {
        labels: {
          color: textColor,
        },
      },
    },
    scales: {
      x: {
        ticks: {
          color: textColorSecondary,
          font: {
            weight: 500,
          },
        },
        grid: {
          display: false,
          drawBorder: false,
        },
      },
      y: {
        ticks: {
          color: textColorSecondary,
        },
        grid: {
          color: surfaceBorder,
          drawBorder: false,
        },
        suggestedMin: 0,
        suggestedMax: 50,
      },
    },
  };
};
</script>

<template>
  <div class="card">
    <Chart
      type="bar"
      :data="chartData"
      :options="chartOptions"
      class="h-[25rem]"
    />
  </div>
</template>
