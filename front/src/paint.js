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

const computeButton = document.getElementById('computeData')

computeButton.addEventListener('click', e => {

  fetch('http://localhost:8000/compute')
    .then(res => res.text())
    .then(data => console.log({data}))
    .catch(err => console.log({err}))


})


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
