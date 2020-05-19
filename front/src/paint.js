import { indexValues } from './indexValues.mjs'

const data = {
  labels: Array.from({ length: indexValues.length }, (_, i) => i),
  datasets: [
    {
      name: 'index value',
      type: 'line',
      values: indexValues
    }
  ]
}

const loadButton = document.getElementById('loadData')

loadButton.addEventListener('click', e => {
  const chart = new frappe.Chart('#chart', { // or a DOM element,
    // new Chart() in case of ES6 module with above usage
    title: 'Xtal index value',
    data: data,
    type: 'line',
    height: 250,
    colors: ['#7cd6fd']
  })
})
