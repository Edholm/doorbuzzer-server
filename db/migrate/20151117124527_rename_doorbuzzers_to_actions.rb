class RenameDoorbuzzersToActions < ActiveRecord::Migration
  def change
    rename_table :doorbuzzers, :actions
  end
end
