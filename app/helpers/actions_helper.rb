module ActionsHelper
  def checkbox_icon activated
    unless activated
      return fa_icon 'square-o'
    end
    fa_icon 'check-square-o'
  end
end
