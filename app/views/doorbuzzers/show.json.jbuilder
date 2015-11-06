json.extract! @doorbuzzer, :id, :name, :description, :activated, :default_time, :created_at, :updated_at
json.unlock_url unlock_doorbuzzer_url(@doorbuzzer, format: :json)
