json.array!(@doorbuzzers) do |doorbuzzer|
  json.extract! doorbuzzer, :id, :name, :description, :activated, :default_time
  json.unlock_url unlock_doorbuzzer_url(doorbuzzer, format: :json)
end
