class CreateDoorbuzzers < ActiveRecord::Migration
  def change
    create_table :doorbuzzers do |t|
      t.string :name
      t.text :description
      t.boolean :activated
      t.string :password
      t.integer :default_time
      t.string :host
      t.integer :port

      t.timestamps null: false
    end
  end
end
