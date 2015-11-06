class Doorbuzzer < ActiveRecord::Base
  validates :name, :default_time, :host, :port, presence: true
  validates :default_time, numericality: {greater_than_or_equal_to: 500, less_than_or_equal_to: 10000}
  validates :port, numericality: {greater_than: 0, less_than_or_equal_to: 65536}
  validates :password, presence:true, length: {maximum: 100}
  validate :check_whitespace


private
  def check_whitespace
    if self.host.match(/\s+/)
      errors.add(:host, "Whitespace not allowed")
    end
  end
end
