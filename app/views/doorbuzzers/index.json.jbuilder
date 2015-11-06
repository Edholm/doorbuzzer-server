json.array!(@doorbuzzers) do |doorbuzzer|
  json.extract! doorbuzzer, :id, :name, :description, :activated, :password, :default_time, :host, :port
  json.url doorbuzzer_url(doorbuzzer, format: :json)
end
