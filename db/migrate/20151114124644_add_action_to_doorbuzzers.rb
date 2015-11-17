class AddActionToDoorbuzzers < ActiveRecord::Migration
  def change
    add_column :doorbuzzers, :action, :string
  end
end
