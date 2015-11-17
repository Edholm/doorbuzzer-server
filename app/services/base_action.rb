class BaseAction
  def execute(hash = nil)
    yield hash if block_given?
  end
end
