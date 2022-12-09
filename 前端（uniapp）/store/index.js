import Vue from 'vue'
import Vuex from 'vuex'
// import axios from 'axios'

Vue.use(Vuex);

export default new Vuex.Store({
	state: {
		Integral: null,

	},
	mutations: {
		EDIT(state, value) {
			state.Integral = value
			
		},
		
	},
	actions: {},
	getters: {}
})
